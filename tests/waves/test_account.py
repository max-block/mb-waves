from mb_waves.waves import account


def test_generate_new_account():
    new_acc = account.generate_new_account()
    assert len(new_acc.address) > 10 and len(new_acc.seed) > 10 and len(new_acc.private_key) > 10

    new_acc_2 = account.generate_new_account()
    assert new_acc.address != new_acc_2.address


def test_check_private_key():
    assert account.check_private_key("3P7aeS1nSqqhUVuhmoCngMo7QoaqAVyEMey", "5s9yQQwpGjMCVHrxgJochVFWwHbejHxfYfoaWMUgCtjh")
    assert not account.check_private_key("3P7aeS1nSqqhUVuhmoCngMo7QoaqAVyEMey", "CuAVscQRV7ydxjtf3cwMeF9oSArPmLXcG5sdXNY5ivRY")


def test_is_valid_address():
    assert account.is_valid_address("3P7aeS1nSqqhUVuhmoCngMo7QoaqAVyEMey")
    assert not account.is_valid_address("3P7aeS1nSqqhUVuhmoCngMo7QoaqAVyEMey1")
