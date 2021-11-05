from aiogram.dispatcher.filters.state import State, StatesGroup

class state(StatesGroup):
    ZERO = State()
    READY = State()
    SPORT = State()



class admin(StatesGroup):
    WAITING_SENDING = State()
    APPROVE = State()
    SECOND_APPROVE =State()