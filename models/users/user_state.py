# from abc import ABC, abstractmethod

# # Abstract State
# class UserState(ABC):
#     @abstractmethod
#     def request_access(self):
#         pass

# # Concrete State: Blocked
# class BlockedState(UserState):
#     def blocked(self):
#         print("Access Denied: Your account has been blocked\n")

# # Concrete State: Unblocked
# class UnblockedState(UserState):
#     def unblocked(self):
#         print("Access Granted. Welcome!\n")

# # Context Class
# class User:
#     def __init__(self):
#         # User starts in an Unblocked State
#         self.state = UnblockedState()

#     def request_access(self):
#         self.state.request_access

#     def block_user(self):
#         self.state = BlockedState()

#     def unblock_user(self):
#         self.state = UnblockedState()