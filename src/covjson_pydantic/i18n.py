from enum import Enum
from typing import Dict


class LanguageTag(str, Enum):
    dutch = "nl"
    english = "en"
    german = "de"
    undefined = "und"


# TODO: This was throwing warning:
#   Expected `definition-ref` but got `LanguageTag` - serialized value may not be as expected
# This may be a bug in Pydantic: https://github.com/pydantic/pydantic/issues/6467
# So, for now, reverted to a less strict type
# i18n = Dict[LanguageTag, str]
i18n = Dict[str, str]
