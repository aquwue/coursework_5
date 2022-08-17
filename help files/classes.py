
@dataclass
class UnitClass(Abc):
    name: str = NotImplemented
    max_health: float = NotImplemented
    max_stamina: float = NotImplemented
    attack: float = NotImplemented
    stamina: float = NotImplemented
    armor: float = NotImplemented
    skill: Skill = NotImplemented


class Warrior(UnitClass):  # TODO Инициализируем экземпляр класса UnitClass и присваиваем ему необходимые значения аттрибуотов
    name = 'Воин'
    max_health: float = 60.0
    max_stamina: float = 30.0
    stamina: float = 0.8
    attack: float = 0.9
    armor: float = 1.2
    skill: Skill = ferocious_kick


class Thief(UnitClass):     # TODO действуем так же как и с войном
    name = 'Вор'
    max_health: float = 50.0
    max_stamina: float = 30.0
    stamina: float = 1.5
    attack: float = 1.2
    armor: float = 1.0
    skill: Skill = powerful_thrust


unit_classes = {
    Thief.name: Thief,
    Warrior.name: Warrior
}