import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class SortingAlgorithms {
	static Random rand = new Random();
	
	public static void main(String[] args) {
		int start_n = 1000;
		int factor = 10;
		int limit = 10000000;
		for (int n = start_n; n <= limit; n*=factor) {
			List<Integer> test = getList(n);
			List<Integer> test_merge = new ArrayList<Integer>();
			List<Integer> test_quick = new ArrayList<Integer>();
			
			test_merge.addAll(test);
			long clock = System.currentTimeMillis();
			test_merge = merge_sort(test_merge);
			long mergeDelta = System.currentTimeMillis() - clock;
			if (!isSorted(test_merge)) {
				System.out.println("Error: test_merge not sorted.");
			}
			
			test_quick.addAll(test);
			clock = System.currentTimeMillis();
			test_merge = quick_sort(test_quick);
			long quickDelta = System.currentTimeMillis() - clock;
			if (!isSorted(test_merge)) {
				System.out.println("Error: test_merge not sorted.");
			}
			
			System.out.println("For n = " + n + ", mergeDelta = " + mergeDelta + ", quickDelta = " + quickDelta);
		}
		List<Integer> test = getList(100);
		long clock = System.currentTimeMillis();
		test = quick_sort(test);
		long time = System.currentTimeMillis()-clock;
		System.out.println("Sort completed in " + time + "ms. Verification: sorted = " + isSorted(test));
	}
	
	private static boolean isSorted(List<Integer> arr) {
		if (arr.size() < 2) {
			return true;
		} else {
			for (int i = 1; i < arr.size(); i++) {
				if (arr.get(i) < arr.get(i-1)) {
					return false;
				}
			}
			return true;
		}
	}

	private static List<Integer> getList(int n) {
		List<Integer> result = new ArrayList<Integer>();
		for (int i = 0; i < n; i++) {
			result.add(rand.nextInt());
		}
		return result;
	}
	
	public static List<Integer> quick_sort(List<Integer> arr) {
		if (arr.size() < 2) {
			return arr;
		} else {
			int pivot = arr.remove(0);
			List<Integer> left = new ArrayList<Integer>();
			List<Integer> right = new ArrayList<Integer>();
			for (Integer i : arr) {
				if (i < pivot) {
					left.add(i);
				} else {
					right.add(i);
				}
			}
			left = quick_sort(left);
			right = quick_sort(right);
			left.add(pivot);
			left.addAll(right);
			return left;
		}
	}

	public static List<Integer> merge_sort(List<Integer> arr) {
		return merge_sort(arr.subList(0, arr.size()/2), arr.subList(arr.size()/2, arr.size()));
	}

	private static List<Integer> merge_sort(List<Integer> left, List<Integer> right) {
		if (left.size() > 1)
			left = merge_sort(left);
		if (right.size() > 1)
			right = merge_sort(right);
		List<Integer> temp = new ArrayList<Integer>();
		int l_itr = 0;
		int r_itr = 0;
		while (temp.size() != left.size() + right.size()) {
			if (r_itr == right.size() || (l_itr < left.size() && left.get(l_itr) < right.get(r_itr))) {
				temp.add(left.get(l_itr));
				l_itr++;
			} else {
				temp.add(right.get(r_itr));
				r_itr++;
			}
		}
		return temp;
	}

}
