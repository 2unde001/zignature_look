package com.object;

public class MusicInstruments
{
    String guitar;
    int numberOfDrums;
    boolean rockStarUsesIt;


    // Java naming conventions
    public String getGuiter()
    {
        System.out.println("My favourite guitar is " + guitar);
        return guitar;
    }

    public String setGuitar(String value){
        guitar = value;
        return guitar;
    }

    public int getNumberOfDrums()
    {
        System.out.println("My favourite guitar is " + numberOfDrums);
        return numberOfDrums;
    }



    public int setNumberOfDrums(int value)
    {
        numberOfDrums = value;
        return numberOfDrums;
    }

    public boolean getArockStarUsesIt()
    {
        System.out.println("It always " + rockStarUsesIt + " to use it");
        return rockStarUsesIt;

    }

    public boolean setRockStarUsesIt(boolean value)
    {
        rockStarUsesIt = value;
        return true;
    }

}
