package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing06 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing06 frame = new MySwing06();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 265, 385);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("출력단수:");
		lbl.setBounds(34, 23, 57, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(117, 20, 102, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(34, 48, 185, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(34, 81, 185, 242);
		contentPane.add(ta);
	}
	void myClick() {
		int dan = Integer.parseInt(tf.getText());
		
		String txt ="";
		for(int i = 1; i <= 9;i++) {
			int result = dan*i;
			System.out.println(dan+" X "+i+" = "+result);
			txt += dan+" X "+i+" = "+result + "\n";
		}
		ta.setText(txt);
	}
}
