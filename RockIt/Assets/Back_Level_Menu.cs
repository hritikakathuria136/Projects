using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Back_Level_Menu : MonoBehaviour
{
     public void BacktoLevel()
    {
        SceneManager.LoadScene("Level_Menu");
    }
}
