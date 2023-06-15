 public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // create dummy list
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        // initialize carry as zero, so it can enter the loop
        int carry = 0;
        // Continue looping until these conditions are met; note carry == 1 means that more cal is needed
        while (l1 != null || l2 != null || carry == 1) {
            int sum = 0;
            //  add l1 to sum and move to the next element in l1
            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }
            // same for l2
            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }
            sum += carry;
            // if there is a carry from a 2-digit num, divide the sum by 10 to obtain the value of the carry
            carry = sum / 10;
            // to get the 1's place digit from the carry, add that value to the list
            ListNode node = new ListNode(sum % 10);
            // update ptrs
            cur.next = node;
            cur = cur.next;
        }
        // return the dummy's next for the res list
        return dummy.next;
    }
