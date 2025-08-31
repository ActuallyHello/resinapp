import logging
from typing import Optional, List

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from apps.resinauth.models import Person
from apps.resincore.exceptions.exceptions import LogicalException, TechnicalException


class PersonService:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_by_id(self, id: int) -> Optional[Person]:
        person = Person.objects.filter(id=id).first()
        self.logger.debug(f"GET PERSON BY ID: {id}. RESULT: {person}")
        return person

    def get_persons_with_limit(self, offset: int = 0, limit: int = 10) -> List[Person]:
        page_size = limit
        page_number = int((offset / page_size) + 1)

        persons = Person.objects.all().order_by("id")
        paginator = Paginator(persons, limit)
        page = paginator.page(page_number)

        result = list(page.object_list)
        self.logger.debug(f"GET ALL PERSONS FROM ${offset} TO ${limit}. COUNT: {len(result)}")
        return result

    def create(self, person: Person) -> Person:
        try:
            person.save()
            self.logger.info(f"CREATED PERSON: {person}")
            return person
        except Exception as e:
            self.logger.exception(f"ERROR WHILE CREATING PERSON: {str(e)}")
            raise TechnicalException(f"Error creating person: {str(e)}") from e

    def delete(self, person: Person):
        try:
            person.delete()
            self.logger.info(f"DELETED PERSON: {person}")
        except Exception as e:
            self.logger.exception(f"ERROR WHILE DELETING PERSON: {str(e)}")
            raise TechnicalException(f"Error deleting person: {str(e)}") from e
