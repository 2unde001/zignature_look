package com.object.test;

import com.object.TapeDeck;
import org.junit.Assert;
import org.junit.Test;

public class TapeDeckTest
{
    @Test
    public void validateTapeRecord()
    {
        TapeDeck tapeDeck = new TapeDeck();

        if (tapeDeck.canRecord == true)
        {
            Assert.assertEquals("tape is playing", tapeDeck.recordATape());
            System.out.print("pass");
        }


    }
}
