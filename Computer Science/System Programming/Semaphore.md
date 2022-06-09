# Semaphore

Synchronization을 위한 툴이다.

- Semaphore S: integer variable
- Counting semaphore
  - integer value can range over an unrestricted domain
- Binary semaphore
  - integer value can range only between 0 and 1
  - Same as a mutex lock
- Can only be accessed via two (atomic) operations
  - Wait() and signal(), which are commonly called P() and V()
  - Wait() or P()
    - waits for semaphore to become positive, then decrements it by 1
  - Signal() or V()
    - increments the semaphore by 1, waking up a waiting P if any

# Lock and Semaphore

Lock의 경우 자물쇠가 하나밖에 없는 형태라고 볼 수 있다.  
한 번에 하나의 thread만을 실행하고 통제할 수만 있다.  
Semaphore은 자물쇠가 여러 개 있는 형태라고 볼 수 있다.

# Semaphore 의 사용 목적

- Mutual exclusion
- Scheduling constraints

# Semaphore 구현

- Block(): process를 waiting queue에 삽입
- Wakeup(): waiting queue에서 process를 꺼낸 뒤 ready queue에 삽입

```
typedef struct {
    int value;
    struct process *list;
} semaphore;
```

```
wait(semaphore *S) {
    S->value--;
    if (S->value < 0) {
        add this process to S->list;
        block();
    }
}
```

```
signal(semaphore *S) {
    S->value++;
    if (S->value <= 0) {
        remove a process P from S->list;
        wakeup(P);
    }
}
```

# Classical Problems of Synchronization

- Bounded-Buffer Problem (Producer-Consumer with Bounded Buffer)
- Readers and Writers Problem
- Dining-Philosphers Problem

## Bounded-Buffer Problem (Producer-Consumer with Bounded Buffer)

**Problem Definiton**

- Produce puts items into a shared buffer
- Consumers takes them out
- _n_ buffers, each can hold one item

Need synchronization to access the buffer

- Only one thread can manipulate the buffer at a time (mutex)
- Producer needs to wait if buffer is full (unitil consumer takes items from the buffer)
- Consumer needs to wait if buffer is empty (until producer puts some items into the buffer)

## Readers and Writers Problem

## Dining-Philosphers Problem
