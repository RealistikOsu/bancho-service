from __future__ import annotations

from enum import IntFlag


class Privileges(IntFlag):
    LOGIN = 1 << 0
    PROFILE_PUBLIC = 1 << 1
    SEND_PUBLIC_MESSAGE = 1 << 2
    SEND_PRIVATE_MESSAGE = 1 << 3
    SCORES_PUBLIC = 1 << 4
    SET_USERPAGE = 1 << 5
    SET_AVATAR = 1 << 6
    CREATE_MATCH = 1 << 7
    JOIN_MATCH = 1 << 8
    RANKING_REQUEST = 1 << 9
    SET_BANNER = 1 << 10
    CREATE_USER_COMMENTS = 1 << 11
