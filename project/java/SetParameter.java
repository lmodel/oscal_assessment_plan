package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  Identifies the parameter that will be set by the enclosed value.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SetParameter  {

  private String param-id;
  private List<String> values;
  private String remarks;

}