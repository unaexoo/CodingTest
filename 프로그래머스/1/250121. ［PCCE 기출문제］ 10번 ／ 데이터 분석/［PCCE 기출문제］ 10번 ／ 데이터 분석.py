def solution(data, ext, val_ext, sort_by):
    answer = []
    dictionary = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    for d in data:
        val = d[dictionary[ext]]
        if val <= val_ext:
            answer.append(d)
    answer = sorted(answer, key=lambda item: item[dictionary[sort_by]])
    return answer
