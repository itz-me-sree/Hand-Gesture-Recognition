import numpy as np


LANDMARKS = {
    "THUMB_MCP": 2,
    "THUMB_IP": 3,
    "THUMB_TIP": 4,

    "INDEX_MCP": 5,
    "INDEX_PIP": 6,
    "INDEX_DIP": 7,
    "INDEX_TIP": 8,

    "MIDDLE_MCP": 9,
    "MIDDLE_PIP": 10,
    "MIDDLE_DIP": 11,
    "MIDDLE_TIP": 12,

    "RING_MCP": 13,
    "RING_PIP": 14,
    "RING_DIP": 15,
    "RING_TIP": 16,

    "LITTLE_MCP": 17,
    "LITTLE_PIP": 18,
    "LITTLE_DIP": 19,
    "LITTLE_TIP": 20
}


FINGER_ANGLE_THRESHOLD = 150


def calculate_angle_3d(a, b, c):

    ba = np.array([
        a.x - b.x,
        a.y - b.y,
        a.z - b.z
    ])

    bc = np.array([
        c.x - b.x,
        c.y - b.y,
        c.z - b.z
    ])

    norm_ba = np.linalg.norm(ba)
    norm_bc = np.linalg.norm(bc)

    if norm_ba == 0 or norm_bc == 0:
        return 0.0

    cosine_angle = np.dot(ba, bc) / (norm_ba * norm_bc)

    cosine_angle = np.clip(cosine_angle, -1.0, 1.0)

    return np.degrees(np.arccos(cosine_angle))


def is_finger_open(mcp, pip, dip):

    angle = calculate_angle_3d(mcp, pip, dip)

    return angle > FINGER_ANGLE_THRESHOLD


def is_thumb_open(landmarks):

    if landmarks[12].y < landmarks[20].y:

        return landmarks[4].y <= landmarks[3].y

    else:

        return landmarks[4].y >= landmarks[3].y


def get_thumb_direction(landmarks):

    thumb_mcp = landmarks[LANDMARKS["THUMB_MCP"]]
    thumb_tip = landmarks[LANDMARKS["THUMB_TIP"]]

    dy = thumb_tip.y - thumb_mcp.y

    if dy < 0:
        return "UP"

    elif dy > 0:
        return "DOWN"

    return "UNKNOWN"


def identify_gesture(finger_state, thumb_direction):

    if not any(finger_state.values()):
        return "FIST"

    if all(finger_state.values()):
        return "OPEN_PALM"

    if (
        finger_state["INDEX"]
        and not finger_state["MIDDLE"]
        and not finger_state["RING"]
        and not finger_state["LITTLE"]
    ):
        return "POINTING"

    if (
        finger_state["INDEX"]
        and finger_state["MIDDLE"]
        and not finger_state["RING"]
        and not finger_state["LITTLE"]
    ):
        return "VICTORY"

    if (
        finger_state["THUMB"]
        and finger_state["LITTLE"]
        and not finger_state["INDEX"]
        and not finger_state["MIDDLE"]
        and not finger_state["RING"]
    ):
        return "CALL_ME"

    if (
        finger_state["THUMB"]
        and thumb_direction == "UP"
        and not finger_state["INDEX"]
        and not finger_state["MIDDLE"]
        and not finger_state["RING"]
        and not finger_state["LITTLE"]
    ):
        return "THUMBS_UP"

    if (
        finger_state["THUMB"]
        and thumb_direction == "DOWN"
        and not finger_state["INDEX"]
        and not finger_state["MIDDLE"]
        and not finger_state["RING"]
        and not finger_state["LITTLE"]
    ):
        return "THUMBS_DOWN"

    return "UNKNOWN"