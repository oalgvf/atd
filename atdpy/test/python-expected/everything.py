"""Generated by atdpy from everything.atd.

This implements classes for the types defined in 'everything.atd', providing
methods and functions to convert data from/to JSON.
"""

from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import json


def _atd_missing_json_field(type_name: str, json_field_name: str):
    raise ValueError(f"missing field '{json_field_name}'"
                     f" in JSON object of type '{type_name}'")


def _atd_bad_json(expected_type: str, json_value: Any):
    value_str = str(json_value)
    if len(value_str) > 200:
        value_str = value_str[:200] + '…'

    raise ValueError(f"incompatible JSON value where"
                     f" type '{expected_type}' was expected: '{value_str}'")


def _atd_bad_python(expected_type: str, json_value: Any):
    value_str = str(json_value)
    if len(value_str) > 200:
        value_str = value_str[:200] + '…'

    raise ValueError(f"incompatible Python value where"
                     f" type '{expected_type}' was expected: '{value_str}'")


def _atd_read_unit(x: Any) -> None:
    if x is None:
        return x
    else:
        return _atd_bad_json('unit', x)


def _atd_read_bool(x: Any) -> bool:
    if isinstance(x, bool):
        return x
    else:
        return _atd_bad_json('bool', x)


def _atd_read_int(x: Any) -> int:
    if isinstance(x, int):
        return x
    else:
        return _atd_bad_json('int', x)


def _atd_read_float(x: Any) -> float:
    if isinstance(x, (int, float)):
        return x
    else:
        return _atd_bad_json('float', x)


def _atd_read_string(x: Any) -> str:
    if isinstance(x, str):
        return x
    else:
        return _atd_bad_json('str', x)


def _atd_read_list(read_elt: Callable[[Any], Any]) \
        -> Callable[[List[Any]], List[Any]]:
    def read_list(elts: List[Any]) -> List[Any]:
        if isinstance(elts, list):
            return [read_elt(elt) for elt in elts]
        else:
            _atd_bad_json('array', elts)
    return read_list


def _atd_read_nullable(read_elt: Callable[[Any], Any]) \
        -> Callable[[Optional[Any]], Optional[Any]]:
    def read_nullable(x: Any) -> Any:
        if x is None:
            return None
        else:
            return read_elt(x)
    return read_nullable


def _atd_write_unit(x: Any) -> None:
    if x is None:
        return x
    else:
        return _atd_bad_python('unit', x)


def _atd_write_bool(x: Any) -> bool:
    if isinstance(x, bool):
        return x
    else:
        return _atd_bad_python('bool', x)


def _atd_write_int(x: Any) -> int:
    if isinstance(x, int):
        return x
    else:
        return _atd_bad_python('int', x)


def _atd_write_float(x: Any) -> float:
    if isinstance(x, (int, float)):
        return x
    else:
        return _atd_bad_python('float', x)


def _atd_write_string(x: Any) -> str:
    if isinstance(x, str):
        return x
    else:
        return _atd_bad_python('str', x)


def _atd_write_list(write_elt: Callable[[Any], Any]) \
        -> Callable[[List[Any]], List[Any]]:
    def write_list(elts: List[Any]) -> List[Any]:
        if isinstance(elts, list):
            return [write_elt(elt) for elt in elts]
        else:
            _atd_bad_python('list', elts)
    return write_list


def _atd_write_nullable(write_elt: Callable[[Any], Any]) \
        -> Callable[[Optional[Any]], Optional[Any]]:
    def write_nullable(x: Any) -> Any:
        if x is None:
            return None
        else:
            return write_elt(x)
    return write_nullable


class Root_:
    """Case 'Root' of type 'kind' (class 'Kind')."""

    def __repr__(self):
        return self.to_json_string()

    def to_json(self):
        return 'Root'

    def to_json_string(self, **kw) -> str:
        return json.dumps(self.to_json(), **kw)


class Thing:
    """Case 'Thing' of type 'kind' (class 'Kind')."""

    def __init__(self, value):
        self._value: int = value

    def __repr__(self):
        return self.to_json_string()

    @property
    def value(self):
        return self._value

    def to_json(self):
        return ['Thing', _atd_write_int(self._value)]

    def to_json_string(self, **kw) -> str:
        return json.dumps(self.to_json(), **kw)


class WOW:
    """Case 'WOW' of type 'kind' (class 'Kind')."""

    def __repr__(self):
        return self.to_json_string()

    def to_json(self):
        return 'wow'

    def to_json_string(self, **kw) -> str:
        return json.dumps(self.to_json(), **kw)


class Amaze:
    """Case 'Amaze' of type 'kind' (class 'Kind')."""

    def __init__(self, value):
        self._value: List[str] = value

    def __repr__(self):
        return self.to_json_string()

    @property
    def value(self):
        return self._value

    def to_json(self):
        return ['!!!', _atd_write_list(_atd_write_string)(self._value)]

    def to_json_string(self, **kw) -> str:
        return json.dumps(self.to_json(), **kw)


class Kind:
    def __init__(self, value):
        self._value: Union[Root_, Thing, WOW, Amaze] = value

    def __repr__(self):
        return self._value.to_json_string()

    @classmethod
    def from_json(cls, x: Any):
        if isinstance(x, str):
            if x == 'Root':
                return cls(Root_())
            if x == 'wow':
                return cls(WOW())
            _atd_bad_json('Kind', x)
        if isinstance(x, List) and len(x) == 2:
            cons = x[0]
            if cons == 'Thing':
                return cls(Thing(_atd_read_int(x[1])))
            if cons == '!!!':
                return cls(Amaze(_atd_read_list(_atd_read_string)(x[1])))
            _atd_bad_json('Kind', x)
        _atd_bad_json('Kind', x)

    def to_json(self):
        return self._value.to_json()

    @classmethod
    def from_json_string(cls, x: str):
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw) -> str:
        return json.dumps(self.to_json(), **kw)


class Alias:
    """Original type: alias"""

    def __init__(self, x: List[int]):
        self._value: List[int] = x

    def __repr__(self):
        return self.to_json_string()

    @classmethod
    def from_json(cls, x: Any):
        return cls(_atd_read_list(_atd_read_int)(x))

    def to_json(self) -> Any:
        return _atd_write_list(_atd_write_int)(self._value)

    @classmethod
    def from_json_string(cls, x: str):
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw) -> str:
        return json.dumps(self.to_json(), **kw)


class Root:
    """Original type: root"""

    def __init__(
        self,
        *,
        id: str,
        await_: bool,
        __init__: float,
        items: List[List[int]] = [],
        maybe: Optional[int] = None,
        extras: List[int] = [],
        answer: int = (42),
        aliased: Alias,
        point: Tuple[float, float],
        kinds: List[Kind] = [],
    ):
        self._id = id
        self._await = await_
        self.x____init__ = __init__
        self._items = items
        self._maybe = maybe
        self._extras = extras
        self._answer = answer
        self._aliased = aliased
        self._point = point
        self._kinds = kinds

    def __repr__(self):
        return self.to_json_string()

    @property
    def id(self):
        return self._id

    @property
    def await_(self):
        return self._await

    @property
    def x___init__(self):
        return self.x____init__

    @property
    def items(self):
        return self._items

    @property
    def maybe(self):
        return self._maybe

    @property
    def extras(self):
        return self._extras

    @property
    def answer(self):
        return self._answer

    @property
    def aliased(self):
        return self._aliased

    @property
    def point(self):
        return self._point

    @property
    def kinds(self):
        return self._kinds

    @classmethod
    def from_json(cls, x: Any):
        if isinstance(x, dict):
            if 'id' in x:
                id: str = _atd_read_string(x['id'])
            else:
                _atd_missing_json_field('Root', 'id')
            if 'await' in x:
                await_: bool = _atd_read_bool(x['await'])
            else:
                _atd_missing_json_field('Root', 'await')
            if '__init__' in x:
                __init__: float = _atd_read_float(x['__init__'])
            else:
                _atd_missing_json_field('Root', '__init__')
            if 'items' in x:
                items: List[List[int]] = _atd_read_list(_atd_read_list(_atd_read_int))(x['items'])
            else:
                _atd_missing_json_field('Root', 'items')
            if 'maybe' in x:
                maybe: Optional[int] = _atd_read_int(x['maybe'])
            else:
                maybe = None
            if 'extras' in x:
                extras: List[int] = _atd_read_list(_atd_read_int)(x['extras'])
            else:
                extras = []
            if 'answer' in x:
                answer: int = _atd_read_int(x['answer'])
            else:
                answer = (42)
            if 'aliased' in x:
                aliased: Alias = Alias.from_json(x['aliased'])
            else:
                _atd_missing_json_field('Root', 'aliased')
            if 'point' in x:
                point: Tuple[float, float] = (lambda x: (_atd_read_float(x[0]), _atd_read_float(x[1])) if isinstance(x, list) else _atd_bad_json('array', x))(x['point'])
            else:
                _atd_missing_json_field('Root', 'point')
            if 'kinds' in x:
                kinds: List[Kind] = _atd_read_list(Kind.from_json)(x['kinds'])
            else:
                _atd_missing_json_field('Root', 'kinds')
        else:
            _atd_bad_json('Root', x)
        return cls(
            id=id,
            await_=await_,
            __init__=__init__,
            items=items,
            maybe=maybe,
            extras=extras,
            answer=answer,
            aliased=aliased,
            point=point,
            kinds=kinds,
        )

    def to_json(self) -> Any:
        res: Dict[str, Any] = {}
        res['id'] = _atd_write_string(self._id)
        res['await'] = _atd_write_bool(self._await)
        res['__init__'] = _atd_write_float(self.x____init__)
        res['items'] = _atd_write_list(_atd_write_list(_atd_write_int))(self._items)
        if self._maybe is not None:
            res['maybe'] = _atd_write_int(self._maybe)
        res['extras'] = _atd_write_list(_atd_write_int)(self._extras)
        res['answer'] = _atd_write_int(self._answer)
        res['aliased'] = (lambda x: x.to_json())(self._aliased)
        res['point'] = (lambda x: [_atd_write_float(x[0]), _atd_write_float(x[1])] if isinstance(x, tuple) else _atd_bad_python('tuple', x))(self._point)
        res['kinds'] = _atd_write_list((lambda x: x.to_json()))(self._kinds)
        return res

    @classmethod
    def from_json_string(cls, x: str):
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw) -> str:
        return json.dumps(self.to_json(), **kw)
