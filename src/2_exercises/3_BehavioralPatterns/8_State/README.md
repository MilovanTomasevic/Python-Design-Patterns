## State Coding Exercise
A combination lock is a lock that opens after the right digits have been entered. A lock is preprogrammed with a combination (e.g., `12345` ) and the user is expected to enter this combination to unlock the lock.

The lock has a Status field that indicates the state of the lock. The rules are:
- If the lock has just been locked (or at startup), the status is LOCKED.
- If a digit has been entered, that digit is shown on the screen. As the user enters more digits, they are added to Status.
- If the user has entered the correct sequence of digits, the lock status changes to OPEN.
- If the user enters an incorrect sequence of digits, the lock status changes to ERROR.

Please implement the `CombinationLock`  class to enable this behavior. Be sure to test both correct and incorrect inputs.

Here is an example unit test for the lock:

```py
class FirstTestSuite(unittest.TestCase):
    def test_success(self):
        cl = CombinationLock([1, 2, 3, 4, 5])
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        self.assertEqual('1', cl.status)
        cl.enter_digit(2)
        self.assertEqual('12', cl.status)
        cl.enter_digit(3)
        self.assertEqual('123', cl.status)
        cl.enter_digit(4)
        self.assertEqual('1234', cl.status)
        cl.enter_digit(5)
        self.assertEqual('OPEN', cl.status)
```