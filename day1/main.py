def main():
    elves = []
    curr_elf = 0
    with open("./puzzle_input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            if len(line) == 0:
                elves.append(curr_elf)
                curr_elf = 0
            else:
                curr_elf += int(line.strip())
        elves.append(curr_elf)

    print(sum(sorted(elves)[-3:]))

if __name__ == '__main__':
    main()