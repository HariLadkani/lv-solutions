class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        priority_queue<pair<int, int>> pq;
        unordered_map<int, int> counter;
        vector<int> result;

        for (auto& num: nums) {
            counter[num] += 1;
        }

        for (auto& pair: counter) {
            int value = pair.first;
            int freq = pair.second;
            pq.push({freq, value});
        }

        while (!pq.empty() && k>0) {
            int value = pq.top().second;
            result.push_back(value);
            pq.pop();
            k -= 1;
        }

        return result;
        
    }
};