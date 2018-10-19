import abc
from task_app.models import Task

class TaskState(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def In_New(self, title):
        pass

    @abc.abstractmethod
    def In_Progress(self):
        pass

    @abc.abstractmethod
    def In_Done(self):
        pass

class New(TaskState):
    def In_New(self, id='', title='', description=''):
        print("here", id)
        try:
            obj = Task.objects.get(id=id)
            obj.title = title
            obj.description = description
            obj.save()
        except Task.DoesNotExist:
            obj = Task.objects.create(id=id)

    def In_Progress(self):
        return "wait when New Done"

    def In_Done(self):
        return "waiting everything done to show"


class Progress(TaskState):
    def In_New(self):
        return "U can't edit in this state"

    def In_Progress(self):
        return "call any task by any id"

    def In_Done(self):
        return "waiting everything done to show"


class Done(TaskState):
    def In_New(self):
        return "U can't edit in this state"

    def In_Progress(self):
        return "U can't call any thing in this state"

    def In_Done(self):
        return "show all thing"

class Context(TaskState):
    def __init__(self, state):
        self.state = state

    def set_state(self, state):
        self.state = state

    def In_New(self, id='', title='', description=''):
        return self.state.In_New(id, title, description)

    def In_Progress(self):
        return self.state.In_Progress()

    def In_Done(self):
        return self.state.In_Done()

# if __name__ == '__main__':
#
#     state = context(New())
#     print("New in New state", state.In_New())
#     print("InProgress in New state", state.In_Progress())
#     print("Done in New state", state.In_Done())
#
#     state.set_state(Progress())
#     print("New in InProg state", state.In_New())
#     print("InProgress in InProg state", state.In_Progress())
#     print("Done in New InProg", state.In_Done())
#
#     state.set_state(Done())
#
#     print("New in Done state", state.In_New())
#     print("InProgress in Done state", state.In_Progress())
#     print("Done in New Done", state.In_Done())


# class TaskState(object):
#
#    name = "state"
#    allowed = []
#
#    def switch(self, state, id=''):
#       """ Switch to new state """
#       if state.name in self.allowed:
#          print ('Current:',self,' => switched to new state',state.name)
#          self.__class__ = state
#       else:
#          print( 'Current:',self,' => switching to',state.name,'not possible.')
#
#    def __str__(self):
#       return self.name
#
# class New(TaskState):
#    name = "New"
#    allowed = ['Progress']
#    print(Task.objects.all())
#
# class Progress(TaskState):
#    name = "Progress"
#    allowed = ['New']
#
# class Done(TaskState):
#    name = "Done"
#    allowed = ['New', 'Progress']
#
# class Context(object):
#    def __init__(self, model=' '):
#       self.model = model
#       # State of the computer - default is off.
#       self.state = Done()
#
#    def change(self, state, id=''):
#       """ Change state """
#       self.state.switch(state, id='')

# if __name__ == "__main__":
   # state = Context()
   # state.change(New)
   # state.change(Progress)
   # state.change(Done)
