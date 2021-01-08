
from dataclasses import dataclass

from typing import Any, Dict, List, Optional, Union, get_args, get_origin

def _from_json(cls, data):
    if data is None or cls in [bool, int, float, str, object] or cls is Any:
        return data
    if get_origin(cls) is Union:
        return _from_json(get_args(cls)[0], data)
    if get_origin(cls) is list:
        return [_from_json(get_args(cls)[0], d) for d in data]
    if get_origin(cls) is dict:
        return { k: _from_json(get_args(cls)[1], v) for k, v in data.items() }
    return cls.from_json(data)

def _to_json(data):
    if data is None or type(data) in [bool, int, float, str, object]:
        return data
    if type(data) is list:
        return [_to_json(d) for d in data]
    if type(data) is dict:
        return { k: _to_json(v) for k, v in data.items() }
    return data.to_json()
@dataclass
class RootOverrideTypeDiscriminatorBaz(object):
    """

    """



    @classmethod
    def from_json(cls, data) -> "RootOverrideTypeDiscriminatorBaz":
        """
        Construct an instance of this class from parsed JSON data.
        """

        return cls(
            "baz",

        )

    def to_json(self):
        """
        Generate JSON-ready data from an instance of this class.
        """

        out = {}
        out["foo"] = "baz"

        return out
@dataclass
class Root:
    """

    """


    OverrideElementsContainer: 'List[str]'
    """

    """


    OverrideTypeDiscriminator: 'object'
    """

    """


    OverrideTypeEnum: 'object'
    """

    """


    OverrideTypeExpr: 'object'
    """

    """


    OverrideTypeProperties: 'object'
    """

    """


    OverrideValuesContainer: 'Dict[str, str]'
    """

    """



    @classmethod
    def from_json(cls, data) -> "Root":
        """
        Construct an instance of this class from parsed JSON data.
        """

        return cls(

            _from_json(List[str], data.get("override_elements_container")),

            _from_json(object, data.get("override_type_discriminator")),

            _from_json(object, data.get("override_type_enum")),

            _from_json(object, data.get("override_type_expr")),

            _from_json(object, data.get("override_type_properties")),

            _from_json(Dict[str, str], data.get("override_values_container")),

        )

    def to_json(self):
        """
        Generate JSON-ready data from an instance of this class.
        """

        out = {}

        
        out["override_elements_container"] = _to_json(self.OverrideElementsContainer)
        

        
        out["override_type_discriminator"] = _to_json(self.OverrideTypeDiscriminator)
        

        
        out["override_type_enum"] = _to_json(self.OverrideTypeEnum)
        

        
        out["override_type_expr"] = _to_json(self.OverrideTypeExpr)
        

        
        out["override_type_properties"] = _to_json(self.OverrideTypeProperties)
        

        
        out["override_values_container"] = _to_json(self.OverrideValuesContainer)
        

        return out