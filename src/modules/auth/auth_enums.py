from enum import Enum

class FlowType(str, Enum):
    C2B = "C2B"
    B2B = "B2B"

class LoginType(str, Enum):
    BASIC = "basic"
    GOOGLE = "google" 
    GITHUB = "github"
    MICROSOFT = "microsoft"