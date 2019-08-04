from typing import Union


class Timer():  # noqa: D101
    def __init__(self, description: str, duration: int, is_work: bool,
                 autopause: bool, beeps_per_second: int):  # noqa: D107
        self.description = description
        self.duration = duration
        self.is_work = is_work
        self.autopause = autopause
        self.beeps_per_second = beeps_per_second

    def __str__(self) -> str:  # noqa: D105
        is_work = 'WORK' if self.is_work else 'REST'
        duration = int(self.duration / 1000)
        return f"""<TIMER. {self.description} {duration}" {is_work}>"""


def add_entry(plan: list, entry: Union['Timer', 'Loop'], position: int):  # noqa: D103
    if position:
        plan.insert(position, entry)
    else:
        plan.append(entry)
    return plan


class Loop():  # noqa: D101
    def __init__(self, *, description: str, rounds: int):  # noqa: D107
        self.description = description
        self.rounds = rounds
        self.plan = []

    def add_timer(self, timer: 'Timer', position: int = None):  # noqa: D102
        self.plan = add_entry(self.plan, timer, position)

    def __str__(self) -> str:  # noqa: D105
        result = f"<LOOP. {self.description} {self.rounds}>\n"
        for item in self.plan:
            result += f"  {item.__str__()}\n"
        return result


class Plan():  # noqa: D101
    def __init__(self, *, name, description):  # noqa: D107
        self.name = name
        self.description = description
        self.plan = []

    def add_timer(self, timer: 'Timer', position: int = None):  # noqa: D102
        self.plan = add_entry(self.plan, timer, position)

    def add_loop(self, loop: 'Loop', position: int = None):  # noqa: D102
        self.plan = add_entry(self.plan, loop, position)

    def __str__(self) -> str:  # noqa: D105
        result = f"<PLAN. {self.name}: {self.description}>\n"
        for item in self.plan:
            formatted_lines = item.__str__().split('\n')
            for line in formatted_lines:
                if len(line) > 1:
                    result += f"  {line}\n"
        return result[:-1]


# press = Timer(description='Description', duration=1000, is_work=True,
#               autopause=False, beeps_per_second=0)
# loop = Loop(description='Loop description', rounds=2)
# loop.add_timer(press)
# plan = Plan(name='Super plan', description='nahh...lazy')
# plan.add_timer(press)
# plan.add_loop(loop)
