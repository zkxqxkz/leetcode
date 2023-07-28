
func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)
    for i, num  := range nums {
        candidate := target - num
        if idx, found := seen[num]; found {
			return []int{idx, i}
        }
        seen[candidate] = i
    }
    return []int{}
    
}
