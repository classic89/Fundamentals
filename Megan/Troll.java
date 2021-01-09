package Megan;

// Disemvowel Trolls
public class Troll {
  public static String disemvowel(String str) {
    // Code away...
    String vowel_less = str;
    char vowels[] = { 'a', 'e', 'i', 'o', 'u' };
    for (int letterPosition = 0; letterPosition < str.length(); letterPosition++) {
      System.out.print(letterPosition);
    }
    return vowel_less;
  }

  public static String hello() {
    String greeting = "I live!";
    return greeting;
  }

  public static void main(String[] args) {
    String hello = hello();
    System.out.println(hello);
    System.out.println(disemvowel(hello));

  }
}