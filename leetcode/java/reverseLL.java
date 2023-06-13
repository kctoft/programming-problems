public class Main {
  public static ListNode reverse(ListNode head) {
    ListNode cur = head;
    ListNode prev = null;

    while (cur != null) {
      // save cur.next into a temp variable
      ListNode next = cur.next;

      // start building the rev LL
      cur.next = prev;

      // update ptrs each iteration
      prev = cur;
      cur = next;
    }

    //  return the reverse LL (prev is the new head)
    return prev;
  }
}

// display the LL
public static void print(ListNode head) {
  ListNode cur = head;
  while (cur != null) {
    System.out.print(cur.data + " -> ");
    cur = cur.next;
  }
  System.out.print("null");
}

public static void main(String[] agrs) {
  int[] keys = {
    1,
    2,
    3,
    4,
    5
  };

  ListNode node = null;

  for (int i = keys.length -1; i >= 0; i--) {
    node = new ListNode(keys[i], node);
  }

  print(node);
  System.out.println();
  ListNode revNode = reverse(node);
  print(revNode);
}

class ListNode {
  // node class had data and a next pointer
  int data;
  ListNode next;

  // constructor
  ListNode(int d, ListNode node) {
    data = d;
    next = node;
  }
}

/**
 * Expected Output:
 * 1 -> 2 -> 3 -> 4 -> 5 -> null
 * 5 -> 4 -> 3 -> 2 -> 1 -> null
 * */
