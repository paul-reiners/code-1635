from three_state_totalistic_ca import TotalisticCell1D


class TestThreeStateTotalisticCA:
    def test_step(self):
        rule_num = 777
        gen_count = 4
        ca = TotalisticCell1D(rule_num, gen_count)
        ca.start_single()
        for i in range(3):
            ca.step()
        expected_values = \
            [[0, 0, 0, 0, 1, 0, 0, 0, 0,],
             [0, 0, 0, 1, 1, 1, 0, 0, 0,],
             [0, 0, 1, 2, 1, 2, 1, 0, 0,],
             [0, 1, 1, 0, 0, 0, 1, 1, 0,]]
        assert len(ca.array) == len(expected_values)
        for i in range(len(expected_values)):
            assert len(expected_values[i]) == len(ca.array[i])
            for j in range(len(expected_values[i])):
                assert expected_values[i][j] == ca.array[i][j]
