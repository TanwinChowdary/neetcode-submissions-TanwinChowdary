public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length){
            return false;
        }
        Dictionary<char, int> Count_s = new Dictionary<char,int>();
        Dictionary<char, int> Count_t = new Dictionary<char,int>();
        for (int i=0; i<s.Length; i++){
            Count_s[s[i]] = Count_s.GetValueOrDefault(s[i],0)+1;
            Count_t[t[i]] = Count_t.GetValueOrDefault(t[i],0)+1;

        }
        return Count_s.Count == Count_t.Count && !Count_s.Except(Count_t).Any();

    }
}
