using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class Reset_name : MonoBehaviour
{
    public void ResetSavedGame(){
        PlayerPrefs.DeleteKey("player");
        SceneManager.LoadScene("Welcome");
    }
}
