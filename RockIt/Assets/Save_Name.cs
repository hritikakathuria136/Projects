using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Save_Name : MonoBehaviour
{
    public InputField textBox;
    
    public void Start() {
    
    	string playerName = PlayerPrefs.GetString("player");
    	if (playerName.Length > 0) {
    		textBox.text = playerName;
    	}
    
    }

    public void clickSaveButton(){
        PlayerPrefs.SetString("player", textBox.text);
        PlayerPrefs.Save();
        Debug.Log("Your name is " + PlayerPrefs.GetString("player"));
    }
    
}
