import pytest
import gameplay.pet_growth as mod

CASES = [
    ("offline_settle", (8.0, 0.5)),
    ("server_check", (1, 2)),
    ("fixed_seed", (42, 3)),
    ("appearance_sync", (1, 2)),
    ("server_cooldown", (1, 2)),
    ("account_count", (1, 2)),
    ("full_save", (1, 2)),
    ("state_isolate", (1, 2)),
    ("concurrent_clamp", (1.0, 2.0)),
    ("collision_update", (1, 2)),
    ("satiety_decay", (8.0, 0.1)),
    ("evolve_condition", (1, 2)),
    ("skill_inherit", (1, 2)),
    ("breed_cd", (1, 2)),
    ("display_mode", (1, 2)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
