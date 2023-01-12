using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class LevelToGameCheck : MonoBehaviour
{
    public void GotoMenu()
    {
        SceneManager.LoadScene("Game_Menu_Check it");
    }
}
