func distinctSubstringofString(s string, t string) int {
	var count int
	var m map[string]bool
	for i := 0; i < len(s); i++ {
		m = make(map[string]bool)
		for j := i; j < len(s); j++ {
			if m[s[j:j+1]] {
				continue
			}
			if strings.Contains(t, s[j:j+1]) {
				count++
			}
			m[s[j:j+1]] = true
		}
	}
	return count
}