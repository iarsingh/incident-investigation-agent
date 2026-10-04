TOOLS = ["read_logs", "read_deploys", "hypothesize"]
WRITES = ("confirm root cause", "page everyone", "kubectl delete")


class InputError(ValueError):
    pass


def run(goal, payload):
    if not isinstance(goal, str) or not goal.strip():
        raise InputError("goal is empty")
    if any(word in goal.lower() for word in WRITES):
        return {"refused": True, "reason": "This agent only reads or plans. It does not write.", "tools": [], "wrote": False, "applied": False}
    logs = " ".join(payload.get("logs") or []).lower(); result = "memory" if "oom" in logs else "deploy" if "rollout" in logs else "unknown"
    return {"refused": False, "tools": TOOLS, "hypothesis": result, "wrote": False, "applied": False}
