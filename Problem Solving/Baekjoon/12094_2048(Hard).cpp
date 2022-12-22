#include <bits/stdc++.h>

#define endl "\n"
#define MAX 20
using namespace std;

int N, Answer;
int MAP[MAX][MAX];

int Bigger(int A, int B) {
  if (A > B) return A;
  return B;
}

void Input() {
  cin >> N;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cin >> MAP[i][j];
      if (MAP[i][j] > Answer) Answer = MAP[i][j];
    }
  }
}

void Copy_MAP(int A[][MAX], int B[][MAX]) {
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      A[i][j] = B[i][j];
    }
  }
}

int Move(int Dir, int A[][MAX]) {
  int Max_Value = 0;
  if (Dir == 0) {
    for (int i = 0; i < N; i++) {
      int Value = -1;
      int Idx = N;

      for (int j = N - 1; j >= 0; j--) {
        if (A[i][j] == 0) continue;
        if (A[i][j] == Value) {
          A[i][Idx] = A[i][Idx] * 2;
          Value = -1;
        } else {
          Value = A[i][j];
          Idx--;
          A[i][Idx] = A[i][j];
        }

        Max_Value = Bigger(Max_Value, A[i][Idx]);
      }

      for (int j = Idx - 1; j >= 0; j--) A[i][j] = 0;
    }
  } else if (Dir == 1) {
    for (int i = 0; i < N; i++) {
      int Value = -1;
      int Idx = -1;

      for (int j = 0; j < N; j++) {
        if (A[i][j] == 0) continue;

        if (A[i][j] == Value) {
          A[i][Idx] = A[i][Idx] * 2;
          Value = -1;
        } else {
          Value = A[i][j];
          Idx++;
          A[i][Idx] = A[i][j];
        }

        Max_Value = Bigger(Max_Value, A[i][Idx]);
      }

      for (int j = Idx + 1; j < N; j++) A[i][j] = 0;
    }
  } else if (Dir == 2) {
    for (int j = 0; j < N; j++) {
      int Value = -1;
      int Idx = N;

      for (int i = N - 1; i >= 0; i--) {
        if (A[i][j] == 0) continue;

        if (A[i][j] == Value) {
          A[Idx][j] = A[Idx][j] * 2;
          Value = -1;
        } else {
          Value = A[i][j];
          Idx--;
          A[Idx][j] = A[i][j];
        }

        Max_Value = Bigger(Max_Value, A[Idx][j]);
      }

      for (int i = Idx - 1; i >= 0; i--) A[i][j] = 0;
    }
  } else if (Dir == 3) {
    for (int j = 0; j < N; j++) {
      int Value = -1;
      int Idx = -1;

      for (int i = 0; i < N; i++) {
        if (A[i][j] == 0) continue;

        if (A[i][j] == Value) {
          A[Idx][j] = A[Idx][j] * 2;
          Value = -1;
        } else {
          Value = A[i][j];
          Idx++;
          A[Idx][j] = A[i][j];
        }

        Max_Value = Bigger(Max_Value, A[Idx][j]);
      }

      for (int i = Idx + 1; i < N; i++) A[i][j] = 0;
    }
  }
  return Max_Value;
}

bool Same_MAP(int A[][MAX], int B[][MAX]) {
  /* 같은 맵인지 확인하는 함수 */
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (A[i][j] != B[i][j]) return false;
    }
  }
  return true;
}

bool Have_Possible(int Next_Max, int Next_Cnt) {
  /* 현재 움직인 횟수와 최대값을 통해서, 최고의 상황에서의 기댓값을 계산. */
  int Remain_Cnt = 10 - Next_Cnt;
  int Expect_Max = Next_Max * pow(2, Remain_Cnt);

  if (Answer >= Expect_Max) return false;
  return true;
}

void DFS(int Cnt, int State[][MAX], int Max_Value) {
  if (Cnt == 10) {
    Answer = Max_Value;
    return;
  }

  for (int i = 0; i < 4; i++) {
    int nState[MAX][MAX];
    int nMax_Value;
    int nCnt = Cnt + 1;

    Copy_MAP(nState, State);
    nMax_Value = Move(i, nState);

    if (Same_MAP(State, nState) == true) continue;
    if (Have_Possible(nMax_Value, nCnt) == true) DFS(nCnt, nState, nMax_Value);
  }
}

void Solution() {
  DFS(0, MAP, Answer);
  cout << Answer << endl;
}

void Solve() {
  Input();
  Solution();
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  Solve();
}
