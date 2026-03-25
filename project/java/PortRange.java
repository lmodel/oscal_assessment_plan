package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Where applicable, the transport layer protocol port range.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PortRange  {

  private Integer start;
  private Integer end;
  private String transport;
  private String remarks;

}