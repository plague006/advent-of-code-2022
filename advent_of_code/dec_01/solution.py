from advent_of_code.shared_lib.resources import INPUT_FOLDER


def get_elves() -> list[int]:
    input_file = INPUT_FOLDER / "input"
    input_text = input_file.read_text("UTF-8")
    elves_as_text = input_text.split("\n\n")

    elves = []
    for elf_text in elves_as_text:
        if not elf_text:
            continue
        calorie_values_as_text = elf_text.split("\n")
        elves.append(
            sum(int(calorie_value_str) for calorie_value_str in calorie_values_as_text)
        )
    return elves


def get_sum_of_top_n(nums: list[int], n: int) -> int:
    total = 0
    for _ in range(n):
        current_max = max(nums)
        total += current_max
        nums.remove(current_max)

    return total


if __name__ == "__main__":
    elven_calorie_counts = get_elves()
    print(max(elven_calorie_counts))
    print(get_sum_of_top_n(elven_calorie_counts, 3))
