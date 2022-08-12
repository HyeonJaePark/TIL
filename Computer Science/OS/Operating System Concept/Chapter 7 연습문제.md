### 7.1 Windows와 Linux가 여러 락 기법을 구현하는 이유를 설명하라. 그들이 스핀락, mutex락, 세마포 및 조건 변수를 사용하는 환경을 설명하라. 각각의 경우에 그 기법이 필용한 이유를 설명하라.

응용 프로그램 개발자의 필요에 따라 여러 락 기법을 구현하기 때문이다.  
스핀락은 스레드가 대기 큐에 들어가는 오버헤드를 발생시키지 않고 busy loop에서 짧은 시간 동안 실행 될 수 있는 멀티프로세서 시스템에서 유용하다.  
mutex 락은 리소스를 락 할 때 유용하다.  
세마포 및 조건 변수는 자원이 장기간 유지되어야 할 때 동기화에 더 적합한 도구이다.

### 7.2 Windows는 슬림 reader-writer 락이라는 가벼운 동기화 도구를 제공한다. 대부분의 reader-writer 구현은 reader 또는 writer를 선호하거나 FIFO 정책을 사용하여 대기 스레드를 정렬하는 반면에, 슬림 reader-writer는 reader 또는 writer를 선호하지 않으며 대기 스레드를 FIFO 정책에 따라 정렬하지도 않는다. 이러한 동기화 도구를 제공하면 얻을 수 있는 이점을 설명하라.

단순하고 간단한 이점이 있다. 일반적으로 reader-writer 락을 서정하는데 드는 오버헤드는 큰 편이다. 슬림 reader-writer은 이러한 오버헤드를 방지하고 락을 빠르게 설정할 수 있다. 슬림 reader-writer는 빠르게 acquire하고 release 하면서 reader-writer 락이 필요한 경우 사용하면 좋다.

### 7.3 이진 세마포 대신 mutex 락을 사용할 수 있도록 하려면 그림 7.1 및 그림 7.2의 생산자와 소비자 프로세스를 어떻게 변경해야 하는지 설명하라.

```cpp
while (true) {
    /* produce an item in next_produced */

    wait(empty);
    wait(mutex);

    /* add next_produced to the buffer */

    signal(mutex);
    signal(full);
}
```

```cpp
while (true) {
    wait(full);
    wait(mutex);

    /* remove an item from buffer to next_consumed */

    signal(mutex);
    signal(empty);

    /* consume the item in next_consumed */
}
```

wait(mutex)와 signal(mutex)를 acquire(mutex), release(mutex)으로 대체한다.

### 7.4 식사하는 철학자들의 문제에서 교착 상태가 어떻게 가능한지 설명하라.

만약 철학자들이 모두 배고픈 상태여서 자신의 왼편에 있는 젓가락을 집는다면 두 개의 젓가락을 한 번에 집을 수 있는 철학자가 없게 되어서 교착 상태에 빠지게 된다.

### 7.5 Windows dispatcher 객체의 signaled 상태와 nonsignaled 상태의 차이점을 설명하라.

signaled 상태는 객체가 사용 가능하고 그 객체를 얻을 때 그 스데르가 봉쇄되지 않음을 뜻한다.  
nonsignaled 상태는 객체가 사용할 수 없고 그 객체를 얻으려고 시도하면 그 스레드가 봉쇄됨을 뜻한다.

## 7.6 val이 Linux 시스템에서 원자적 정수라고 가정하자. 다음 연산이 완료된 후 val 값은 무엇인가?

```cpp
atomic_set(&val, 10);
atomic_sub(8, &val);
atomic_inc(&val);
atomic_inc(&val);
atomic_add(6, &val);
atomic_sub(3, &val);
```

최종 val 값은 7이다.
