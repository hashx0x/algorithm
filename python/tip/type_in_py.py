from typing import (
    Any, Callable, ClassVar, Generic, Iterable, Iterator, Literal, 
    Optional, Type, TypeVar, Union, overload
)

# 기본 타입 힌트
age: int = 30
name: str = "Alice"
is_active: bool = True
height: float = 170.5

# 복합 타입
numbers: list[int] = [1, 2, 3]
scores: dict[str, float] = {"math": 95.5, "science": 89.0}
coordinates: tuple[int, int] = (10, 20)
mixed_list: list[Union[int, str]] = [1, "two", 3]

# Optional 타입
nickname: Optional[str] = None  # Equivalent to Union[str, None]

# Literal 타입 (고정된 값)
status: Literal["active", "inactive", "banned"] = "active"

# Any 타입
data: Any = {"key": "value"}  # Any 타입은 모든 값을 받을 수 있음

# Callable 타입 (함수)
def apply_function(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)

# 제네릭 (TypeVar)
T = TypeVar('T')  # 일반적인 제네릭
K = TypeVar('K', bound=str)  # str 타입으로 제한된 제네릭

def get_first_item(items: list[T]) -> T:
    return items[0]

# Iterable, Iterator
def process_items(items: Iterable[int]) -> Iterator[int]:
    for item in items:
        yield item * 2

# ClassVar
class Example:
    count: ClassVar[int] = 0  # 모든 인스턴스에서 공유

# Type 힌트
class Base: ...
class Derived(Base): ...

def factory(cls: Type[Base]) -> Base:
    return cls()

# overload (다중 호출 정의)
@overload
def read_file(path: str) -> str: ...
@overload
def read_file(path: bytes) -> bytes: ...

def read_file(path: Union[str, bytes]) -> Union[str, bytes]:
    return path

# Generic 클래스
class Box(Generic[T]):
    def __init__(self, content: T) -> None:
        self.content = content

# 사용 예시
# box = Box 타입 (Python 3.11+)
from typing import Self

class Chainable:
    def set_value(self, value: int) -> Self:
        self.value = value
        return self

chain = Chainable().set_value(10).set_value(20)

# Union 타입 (Python 3.10+에서 | 기호 사용)
value: int | str = "hello"

# TypedDict
from typing import TypedDict

class User(TypedDict):
    id: int
    name: str

user: User = {"id": 1, "name": "Alice"}

# Final (수정 금지)
from typing import Final

PI: Final[float] = 3.14159

# NewType
from typing import NewType

UserId = NewType('UserId', int)
user_id: UserId = UserId(42)

# Protocol (구조적 서브타이핑)
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None:
        print("Drawing a circle")

def render(shape: Drawable) -> None:
    shape.draw()

circle = Circle()
render(circle)
