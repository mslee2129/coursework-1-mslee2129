from user import User


def test_calculate_age(date_of_birth):
    """
    GIVEN a date of birth of a user
    WHEN the date of birth is passed to a calculate_age function
    THEN calculate the age of the user
    """
    user1 = User(first_name='user', last_name='name', email='email@email.com', password='pw', dob=date_of_birth)
    age = user1.calculate_age()
    assert age


def test_hash_password(password):
    """
    GIVEN a user is trying to login
    WHEN the password is not hashed
    THEN hash and store the password
    """
    user2 = User(first_name='user', last_name='name', email='email@email.com', password=password)
    pw = user2.hash_password(password)
    assert pw


def test_is_correct_password_returns_false(password):
    """
    GIVEN a password
    WHEN the password doesn't match the hashed password
    THEN don't accept the login
    """
    user3 = User(first_name='user', last_name='name', email='email@email.com', password=password)
    test_pw = 'Password123'
    is_correct = user3.is_correct_password(test_pw)
    assert is_correct is False


def test_is_correct_password_returns_true(password):
    """
    GIVEN a password
    WHEN the password matches the hashed password
    THEN accept the login
    """
    user3 = User(first_name='user', last_name='name', email='email@email.com', password=password)
    test_pw = 'password123'
    is_correct = user3.is_correct_password(test_pw)
    assert is_correct is True

