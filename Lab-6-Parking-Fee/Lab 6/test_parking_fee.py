
import pytest
from parking_fee import parking_fee, find_slot, monthly_pass


# Parking fee tests
def test_free_short_stay():
    assert parking_fee("car", 20, False, False) == 0


def test_exactly_30_minutes():
    assert parking_fee("bike", 30, False, False) == 0


def test_one_minute_over_free_period():
    assert parking_fee("bike", 31, False, False) == 10


def test_exactly_one_hour():
    assert parking_fee("car", 60, False, False) == 30


def test_round_up_partial_hour():
    assert parking_fee("car", 61, False, False) == 60


def test_truck_fee():
    assert parking_fee("truck", 120, False, False) == 120


def test_bike_ev_discount():
    assert parking_fee("bike", 60, True, False) == 5


def test_car_ev_discount():
    assert parking_fee("car", 60, True, False) == 15


def test_truck_ev_no_discount():
    assert parking_fee("truck", 60, True, False) == 60


def test_lost_ticket_fee():
    assert parking_fee("car", 60, False, True) == 230


def test_ev_and_lost_ticket():
    assert parking_fee("bike", 60, True, True) == 205


def test_unknown_vehicle():
    with pytest.raises(ValueError, match="unknown vehicle"):
        parking_fee("bus", 60, False, False)


def test_negative_duration():
    with pytest.raises(ValueError, match="invalid duration"):
        parking_fee("car", -1, False, False)


# Parking slot tests
def test_parking_full():
    assert find_slot("car", 0, False) == "full"


def test_negative_free_slots():
    assert find_slot("car", -1, False) == "full"


def test_disabled_parking():
    assert find_slot("car", 5, True) == "ground floor"


def test_truck_parking():
    assert find_slot("truck", 5, False) == "basement"


def test_any_floor():
    assert find_slot("car", 5, False) == "any floor"


# Monthly pass tests
def test_bike_monthly_pass():
    assert monthly_pass("bike", False) == 500


def test_resident_bike_monthly_pass():
    assert monthly_pass("bike", True) == 400


def test_car_monthly_pass():
    assert monthly_pass("car", False) == 1500


def test_resident_car_monthly_pass():
    assert monthly_pass("car", True) == 1200


def test_monthly_pass_unknown_vehicle():
    with pytest.raises(ValueError, match="no pass for this vehicle"):
        monthly_pass("truck", False)
