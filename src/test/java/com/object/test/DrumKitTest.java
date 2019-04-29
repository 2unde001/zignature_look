package com.object.test;

import com.object.DrumKit;
import org.junit.Assert;
import org.junit.Test;

public class DrumKitTest
{
    @Test
    public void validateDrumKit()
    {
        DrumKit drumKit = new DrumKit();
        if (drumKit.snare){
            Assert.assertEquals("bang bang ba-bang", drumKit.playSnare());
        }
    }
}
