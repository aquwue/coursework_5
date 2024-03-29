from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    from unit import BaseUnit


@dataclass
class Skill:#(ABC):
    """
    Базовый класс умения
    """
    name: str
    damage: int
    stamina: int
    # user = None
    # target = None
    #
    # @property
    # @abstractmethod
    # def name(self):
    #     pass
    #
    # @property
    # @abstractmethod
    # def stamina(self):
    #     pass
    #
    # @property
    # @abstractmethod
    # def damage(self):
    #     pass
    #
    # @abstractmethod
    # def skill_effect(self) -> str:
    #     pass
    #
    # def _is_stamina_enough(self):
    #     return self.user.stamina > self.stamina
    #
    # def use(self, user: BaseUnit, target: BaseUnit) -> str:
    #     """
    #     Проверка, достаточно ли выносливости у игрока для применения умения.
    #     Для вызова скилла везде используем просто use
    #     """
    #     self.user = user
    #     self.target = target
    #     if self._is_stamina_enough:
    #         return self.skill_effect()
    #     return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."


ferocious_kick = Skill(name='Свирепый пинок', damage=22, stamina=6)
powerful_thrust = Skill(name='Мощный укол', damage=15, stamina=5)



class FuryPunch(Skill):
    name = ...
    stamina = ...
    damage = ...

    def skill_effect(self):
        # TODO логика использования скилла -> return str
        # TODO в классе нам доступны экземпляры user и target - можно использовать любые их методы
        # TODO именно здесь происходит уменшение стамины у игрока применяющего умение и
        # TODO уменьшение здоровья цели.
        # TODO результат применения возвращаем строкой
        pass

class HardShot(Skill):
    name = ...
    stamina = ...
    damage = ...

    def skill_effect(self):
        pass
