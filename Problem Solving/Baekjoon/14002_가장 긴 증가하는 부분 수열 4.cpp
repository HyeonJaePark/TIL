#include <bits/stdc++.h>
using namespace std;

int n;
int arr[1001];
int num[1001];
int seq[1001];

int binarySearch(int start, int end, int val) {
  int mid;
  while (start < end) {
    mid = (start + end) / 2;
    if (arr[mid] >= val) {
      end = mid;
    } else {
      start = mid + 1;
    }
  }
  return end;
}

int main(void) {
  cin >> n;
  int temp;
  int idx = 0;
  for (int i = 0; i < n; i++) {
    cin >> temp;
    num[i] = temp;
    if (i == 0) {
      arr[idx] = temp;
      seq[i] = idx++;
    } else {
      if (temp > arr[idx - 1]) {
        arr[idx] = temp;
        seq[i] = idx++;
      } else {
        int p = binarySearch(0, idx, temp);
        arr[p] = temp;
        seq[i] = p;
      }
    }
  }

  cout << idx << '\n';
  idx--;
  vector<int> v;
  for (int i = n - 1; i >= 0; i--) {
    if (seq[i] == idx) {
      v.push_back(num[i]);
      idx--;
    }
    if (idx == -1) break;
  }
  for (int i = v.size() - 1; i >= 0; i--) {
    cout << v.at(i) << ' ';
  }
}
