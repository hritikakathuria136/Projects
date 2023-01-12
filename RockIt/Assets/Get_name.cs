using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Get_name : MonoBehaviour
{
   public Text NameBox;
   void Start(){
    NameBox.text = PlayerPrefs.GetString("player");
   }
}
