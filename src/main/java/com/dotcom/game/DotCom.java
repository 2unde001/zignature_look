package com.dotcom.game;

public class DotCom
{



    public static void main(String[]args)
    {
       SimpleDotCom simpleDotCom = new SimpleDotCom();

       int[] location = {2,3,4};

       String user = "3";
       simpleDotCom.checkYourSelf(user);
       simpleDotCom.setLocationCell(location);

    }

}
