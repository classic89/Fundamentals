package Megan;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

class TestTroll {
    private Troll t;

    @Before
    public void setUp() throws Exception {
        t = new Troll();
    }

    @Test
    public void sayHello() {
        String test = "I live!";
        assertEquals(test, t.hello());
    }

}