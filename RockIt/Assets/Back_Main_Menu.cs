using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Back_Main_Menu : MonoBehaviour
{
    public void backtoMenu()
    {
        SceneManager.LoadScene("Main_Menu");
    }
}
