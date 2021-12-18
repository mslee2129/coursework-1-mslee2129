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
    GIVEN a password
    WHEN the p
    THEN hash the password
    """
    user2 = User(first_name='user', last_name='name', email='email@email.com', password=password)
    pw = user2.hash_password(password)
    assert pw

def test_is_correct_password(password):
    """
    GIVEN
    WHEN
    THEN
    """
