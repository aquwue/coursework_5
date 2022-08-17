from __future__ import annotations
from abc import ABC, abstractmethod
from equipment import Equipment, Weapon, Armor
from classes import UnitClass
from random import randint
from typing import Optional, Type

BASE_STAMINA_PER_ROUND = 0.4

class BaseUnit(ABC):
    """
    Базовый класс юнита
    """
    def __init__(self, name: str, unit_class: UnitClass, weapon: Weapon, armor: Armor, ):
        """
        При инициализации класса Unit используем свойства класса UnitClass
        """
        self.name = name
        self.unit_class = unit_class
        self.hp = unit_class.max_health
        self.stamina = unit_class.max_stamina
        self.weapon = weapon
        self.armor = armor
        self._is_skill_used: bool = False

    @property
    def health_points(self):
        return round(self.hp, 1)

    @hp.setter
    def health_points(self, value):
        self.hp = value

    @property
    def stamina_points(self):
        return round(self.stamina, 1)

    @stamina.setter
    def stamina_points(self, value):
        self.stamina = value

    def equip_weapon(self, weapon: Weapon):
        # TODO присваиваем нашему герою новое оружие
        return f"{self.name} экипирован оружием {self.weapon.name}"

    def equip_armor(self, armor: Armor):
        # TODO одеваем новую броню
        return f"{self.name} экипирован броней {self.weapon.name}"

    def _count_damage(self, target: BaseUnit) -> int:
        # TODO Эта функция должна содержать:
        #  логику расчета урона игрока
        #  логику расчета брони цели
        #  здесь же происходит уменьшение выносливости атакующего при ударе
        #  и уменьшение выносливости защищающегося при использовании брони
        #  если у защищающегося нехватает выносливости - его броня игнорируется
        #  после всех расчетов цель получает урон - target.get_damage(damage)
        #  и возвращаем предполагаемый урон для последующего вывода пользователю в текстовом виде
        return damage

    def get_damage(self, damage: int) -> Optional[int]:
        # TODO получение урона целью
        #      присваиваем новое значение для аттрибута self.hp
        pass

    @property
    def total_armor(self):
        if sekf.stamina - self.armor.stamina_per_turn >= 0:
            return self.armor.defence * self.unit_class.armor
        return 0

    def hit(self, target: BaseUnit) -> str:
        if self.stamina - self.weapon.stamina_per_hit < 0:
            return  None

        hero_damage = self.weapon.damage * self.unit_class.attack
        dealt_damage = hero_damage - target.total_armor
        if dealt_damage < 0:
            return 0
        self.stamina -= self.weapon.stamina_per_hit
        return round(dealt_damage, 1)

    def take_hit(self, damage:float):
        self.hp -= damage
        if self.hp <0:
            self.hp = 0

    def regenerate_stamina(self):
        delta_stamina = BASE_STAMINA_PER_ROUND * self.unit_class.stamina
        if self.stamina + delta_stamina <= self.unit_class.max_stamina:
            self.stamina += delta_stamina
        else:
            self.stamina = self.unit_class.max_stamina

    def use_skill(self) -> Optional[float]:
        if not self._is_skill_used and self.stamina - self.unit_class.stamina:
            self._is_skill_used = True
            return round(self.unit_class.skill.damage, 1)
        return None

    @abstractmethod
    def hit(self, target: BaseUnit) -> str:
        pass

    def use_skill(self, target: BaseUnit) -> str:
        """
        метод использования умения.
        если умение уже использовано возвращаем строку
        Навык использован
        Если же умение не использовано тогда выполняем функцию
        self.unit_class.skill.use(user=self, target=target)
        и уже эта функция вернем нам строку которая характеризует выполнение умения
        """
        pass


class PlayerUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """
        функция удар игрока:
        здесь происходит проверка достаточно ли выносливости для нанесения удара.
        вызывается функция self._count_damage(target)
        а также возвращается результат в виде строки
        """
        pass
        # TODO результат функции должен возвращать следующие строки:
        f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} соперника и наносит {damage} урона."
        f"{self.name} используя {self.weapon.name} наносит удар, но {target.armor.name} cоперника его останавливает."
        f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."


class EnemyUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """
        функция удар соперника
        должна содержать логику применения соперником умения
        (он должен делать это автоматически и только 1 раз за бой).
        Например, для этих целей можно использовать функцию randint из библиотеки random.
        Если умение не применено, противник наносит простой удар, где также используется
        функция _count_damage(target
        """
        # TODO результат функции должен возвращать результат функции skill.use или же следующие строки:
        f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} и наносит Вам {damage} урона."
        f"{self.name} используя {self.weapon.name} наносит удар, но Ваш(а) {target.armor.name} его останавливает."
        f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."


