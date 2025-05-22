import Foundation

func solution(_ board:[[Int]], _ k:Int) -> Int {
    var result: Int = 0
    for(i, row) in board.enumerated() {
        for (j, value) in row.enumerated() {
            if i + j <= k {
                result += board[i][j]
            }
        }
    }
    return result
}